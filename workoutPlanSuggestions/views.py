import openai
import re
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import WorkoutPreferencesForm, OverallFeedbackForm
from .models import Workout, RecommendationFeedback, SavedWorkoutPlan

# @login_required
# def submit_workout_preferences(request):
#     recommended_text = ""
#     search_done = False

#     saved_plan = SavedWorkoutPlan.objects.filter(user=request.user).first()
#     if saved_plan:
#         recommended_text = saved_plan.plan_html

#     if request.method == "POST" and "submit_preferences" in request.POST:
#         search_done = True
#         form = WorkoutPreferencesForm(request.POST)
#         if form.is_valid():
#             fitness_goal = form.cleaned_data['fitness_goal']
#             available_days = form.cleaned_data['available_days']
#             available_workouts = Workout.objects.filter(fitness_goal=fitness_goal)

#             if available_workouts.exists():
#                 prompt = (
#                     f"You are given a list of workouts from the database. "
#                     f"Only use workouts from this list — do NOT invent new ones. "
#                     f"Create a personalized workout plan based on the user's selected days: {', '.join(available_days)}.\n\n"
#                     "Assign workouts from the list to each selected day. Do not include unselected days.\n"
#                     "Group exercises logically (e.g., Chest, Shoulders, Back, Arms, Legs).\n"
#                     "List exercises for each day with sets and reps.\n"
#                     "Present the output as an HTML table with columns: Day, Muscle Group, Exercises, Sets, Reps.\n\n"
#                     "Workout Options:\n"
#                 )
#                 for workout in available_workouts:
#                     prompt += f"- {workout.name} (Sets: {workout.sets}, Reps: {workout.reps}): {workout.description or ''}\n"

#                 openai.api_key = settings.OPENAI_API_KEY
#                 try:
#                     response = openai.ChatCompletion.create(
#                         model="gpt-3.5-turbo",
#                         messages=[
#                             {"role": "system", "content": "You are a workout recommendation assistant."},
#                             {"role": "user", "content": prompt}
#                         ],
#                         max_tokens=700,
#                         temperature=0.4,
#                     )
#                     content = response.choices[0].message['content']
#                     recommended_text = re.sub(r"```html|```", "", content).strip()

#                     # Inject clickable exercise links using instructions
#                     for workout in available_workouts:
#                         safe_instructions = (workout.instructions or 'No instructions available').replace("'", "\\'")
#                         link = f"<a href='#' onclick=\"showExerciseInstructions('{safe_instructions}'); return false;\">{workout.name}</a>"
#                         recommended_text = recommended_text.replace(workout.name, link)

#                     if saved_plan:
#                         saved_plan.plan_html = recommended_text
#                         saved_plan.save()
#                     else:
#                         SavedWorkoutPlan.objects.create(user=request.user, plan_html=recommended_text)

#                 except Exception as e:
#                     print("OpenAI Error:", e)
#                     recommended_text = "Could not generate recommendation. Please try again."
#             else:
#                 recommended_text = "No workouts available for the selected fitness goal."
#         else:
#             recommended_text = "Invalid form submission."
#     else:
#         form = WorkoutPreferencesForm()

#     overall_feedback_form = OverallFeedbackForm()

#     return render(request, 'workoutPlanSuggestions.html', {
#         'form': form,
#         'recommended_text': recommended_text,
#         'search_done': search_done,
#         'overall_feedback_form': overall_feedback_form,
#     })
@login_required
def submit_workout_preferences(request):
    recommended_text = ""
    search_done = False

    saved_plan = SavedWorkoutPlan.objects.filter(user=request.user).first()
    if saved_plan:
        recommended_text = saved_plan.plan_html

    if request.method == "POST" and "submit_preferences" in request.POST:
        search_done = True
        form = WorkoutPreferencesForm(request.POST)
        if form.is_valid():
            fitness_goal = form.cleaned_data['fitness_goal']
            available_days = form.cleaned_data['available_days']
            available_workouts = Workout.objects.filter(fitness_goal=fitness_goal)

            if available_workouts.exists():
                prompt = (
                    f"You are given a list of workouts from the database. "
                    f"Only use workouts from this list — do NOT invent new ones. "
                    f"Create a personalized workout plan based on the user's selected days: {', '.join(available_days)}.\n\n"
                    "Assign workouts from the list to each selected day. Do not include unselected days.\n"
                    "Group exercises logically (e.g., Chest, Shoulders, Back, Arms, Legs).\n"
                    "List exercises for each day with sets and reps.\n"
                    "Present the output as an HTML table with columns: Day, Muscle Group, Exercises, Sets, Reps.\n\n"
                    "Workout Options:\n"
                )
                for workout in available_workouts:
                    prompt += f"- {workout.name} (Sets: {workout.sets}, Reps: {workout.reps}): {workout.description or ''}\n"

                openai.api_key = settings.OPENAI_API_KEY
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a workout recommendation assistant."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=700,
                        temperature=0.4,
                    )
                    content = response.choices[0].message['content']
                    recommended_text = re.sub(r"```html|```", "", content).strip()

                    # Inject clickable exercise links using modal and video link in the popup only
                    for workout in available_workouts:
                        safe_instructions = (workout.instructions or 'No instructions available').replace("`", "'").replace("\n", "<br>")
                        video_link = f"https://www.youtube.com/results?search_query=how+to+do+{'+'.join(workout.name.split())}+exercise"
                        full_instructions = f"{safe_instructions}<br><br><a href='{video_link}' target='_blank'>Watch video on correct form</a>"
                        hyperlink = f"<a href='#' onclick=\"showExerciseInstructions(`{full_instructions}`); return false;\">{workout.name}</a>"
                        recommended_text = recommended_text.replace(workout.name, hyperlink)

                    if saved_plan:
                        saved_plan.plan_html = recommended_text
                        saved_plan.save()
                    else:
                        SavedWorkoutPlan.objects.create(user=request.user, plan_html=recommended_text)

                except Exception as e:
                    print("OpenAI Error:", e)
                    recommended_text = "Could not generate recommendation. Please try again."
            else:
                recommended_text = "No workouts available for the selected fitness goal."
        else:
            recommended_text = "Invalid form submission."
    else:
        form = WorkoutPreferencesForm()

    overall_feedback_form = OverallFeedbackForm()

    return render(request, 'workoutPlanSuggestions.html', {
        'form': form,
        'recommended_text': recommended_text,
        'search_done': search_done,
        'overall_feedback_form': overall_feedback_form,
    })


@login_required
def submit_feedback(request):
    if request.method == "POST":
        form = OverallFeedbackForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data.get("rating")
            comments = form.cleaned_data.get("comments")
            RecommendationFeedback.objects.create(
                user=request.user,
                rating=rating,
                comments=comments,
            )
    return redirect('submit_workout_preferences')
