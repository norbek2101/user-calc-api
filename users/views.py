from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import Place, UserProfile
from .serializers import UserProfileSerializer  # Assuming a serializer for the UserProfile model

class UserFilterView(APIView):
    def get(self, request):
        total_users_count = UserProfile.objects.count()
        filtered_users_count = 0
        filtered_users = UserProfile.objects.all()

        country_param = request.query_params.get('country', '')
        region_param = request.query_params.get('region', '')
        district_param = request.query_params.get('district', '')
        min_age = request.query_params.get('min_age', 0)
        max_age = request.query_params.get('max_age', 100)

        if country_param:
            selected_country_places = Place.objects.filter(country__name=country_param)
            filtered_users = filtered_users.filter(place__in=selected_country_places)

            if region_param:
                selected_country_region_places = Place.objects.filter(
                    country__name=country_param, region__name=region_param
                )
                filtered_users = filtered_users.filter(place__in=selected_country_region_places)

                if district_param:
                    selected_country_region_distric_places = Place.objects.filter(
                        country__name=country_param, region__name=region_param, district__name=district_param
                    )
                    filtered_users = filtered_users.filter(place__in=selected_country_region_distric_places)

                if min_age and max_age:
                    min_age = int(min_age)  # Ensure numerical types
                    max_age = int(max_age)
                    filtered_users = filtered_users.filter(age__gte=min_age, age__lte=max_age)

        filtered_users_count = filtered_users.count()
        serializer = UserProfileSerializer(filtered_users, many=True)

        return Response({
            'total_users_count': total_users_count,
            'filtered_users_count': filtered_users_count,
            'filtered_users': serializer.data,  # Serialize the filtered users
        }, status=status.HTTP_200_OK)
