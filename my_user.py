from user import Admin

christian = Admin('christian', 'hartzell', 'Admin', 'System Administrator')
christian.describe_user()

print("\nAdding privileges")
christian.privileges.privileges = [
    'can delete posts',
    'can ban user',
    'can create user',
]
# Show updated privileges
christian.privileges.show_privileges()

print(f"\nThe admin Christian has these privileges: ")
christian.privileges.show_privileges()