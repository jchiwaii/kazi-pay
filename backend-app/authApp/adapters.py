from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves the custom fields from the serializer data to the User model.
        """
        user = super().save_user(request, user, form, commit=False)
        data = form.cleaned_data
        
        # Map your custom fields from the serializer to the user model
        user.phone_number = data.get('phone_number')
        user.role = data.get('role')
        user.national_id = data.get('national_id')
        
        if commit:
            user.save()
        return user