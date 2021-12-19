from rest_framework import serializers

from .models import Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = (
            'doctor', 'patient', 'address', 'date', 'price'
        )

    def create(self, validated_data):
        validated_data['doctor'] = self.context['request'].user
        return super().create(validated_data)

    '''
    def update(self, instance, validated_data):
        """Performs an update on a Visit."""

        # Passwords should not be handled with `setattr`, unlike other fields.
        # This is because Django provides a function that handles hashing and
        # salting passwords, which is important for security. What that means
        # here is that we need to remove the password field from the
        # `validated_data` dictionary before iterating over it.

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `Visit` instance one at a time.
            setattr(instance, key, value)

        # Finally, after everything has been updated, we must explicitly save
        # the model. It's worth pointing out that `.set_password()` does not
        # save the model.
        instance.save()
        '''
