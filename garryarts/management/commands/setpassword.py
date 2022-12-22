from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.contrib.auth.models import User

class Command(BaseCommand):
    help="Set a new password for a user"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("username")
        parser.add_argument("password")
        
    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options["username"])
        except User.DoesNotExist:
            raise CommandError(f'Username {options["username"]} invalid.')
        
        user.set_password(options["password"])
        user.save()
        
        self.stdout.write(self.style.SUCCESS(f"Password for {options['username']} successfully changed!"))