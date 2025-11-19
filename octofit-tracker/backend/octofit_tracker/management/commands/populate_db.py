from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Clear existing data
            Activity.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()
            Leaderboard.objects.all().delete()

            # Create teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            # Create users
            ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
            captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
            superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
            batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)

            # Create activities
            Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date='2025-11-19')
            Activity.objects.create(user=captain, type='Cycling', duration=45, calories=400, date='2025-11-18')
            Activity.objects.create(user=superman, type='Swimming', duration=60, calories=500, date='2025-11-17')
            Activity.objects.create(user=batman, type='Yoga', duration=20, calories=100, date='2025-11-16')

            # Create workouts
            Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Medium')
            Workout.objects.create(name='Squats', description='Do 40 squats', difficulty='Easy')
            Workout.objects.create(name='Plank', description='Hold plank for 2 minutes', difficulty='Hard')

            # Create leaderboard
            Leaderboard.objects.create(team=marvel, points=700)
            Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
