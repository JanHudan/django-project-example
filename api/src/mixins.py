from rest_framework import mixins, generics
from rest_framework.response import Response
from django.db.models.query import QuerySet
import json

# import inspect
# lines = inspect.getsource(generics.GenericAPIView)
# print(lines)

# class ListModelMixin:
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset(request))

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

# class RetrieveModelMixin():
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

# class CreateModelMixin():
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# class UpdateModelMixin():
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}

#         return Response(serializer.data)

# class DestroyModelMixin():
#     def destroy(self, request, *args, **kwargs):
        
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class GenericAPIView(views.APIView):
#     """
#     Base class for all other generic views.
#     """
#     # You'll need to either set these attributes,
#     # or override `get_queryset()`/`get_serializer_class()`.
#     # If you are overriding a view method, it is important that you call
#     # `get_queryset()` instead of accessing the `queryset` property directly,
#     # as `queryset` will get evaluated only once, and those results are cached
#     # for all subsequent requests.
#     queryset = None
#     serializer_class = None

#     # If you want to use object lookups other than pk, set 'lookup_field'.
#     # For more complex lookup requirements override `get_object()`.
#     lookup_field = 'pk'
#     lookup_url_kwarg = None

#     # The filter backend classes to use for queryset filtering
#     filter_backends = api_settings.DEFAULT_FILTER_BACKENDS

#     # The style to use for queryset pagination.
#     pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

#     def get_queryset(self):
#         """
#         Get the list of items for this view.
#         This must be an iterable, and may be a queryset.
#         Defaults to using `self.queryset`.

#         This method should always be used rather than accessing `self.queryset`
#         directly, as `self.queryset` gets evaluated only once, and those results
#         are cached for all subsequent requests.

#         You may want to override this if you need to provide different
#         querysets depending on the incoming request.

#         (Eg. return a list of items that is specific to the user)
#         """
#         assert self.queryset is not None, (
#             "'%s' should either include a `queryset` attribute, "
#             "or override the `get_queryset()` method."
#             % self.__class__.__name__
#         )

#         queryset = self.queryset
#         if isinstance(queryset, QuerySet):
#             # Ensure queryset is re-evaluated on each request.
#             queryset = queryset.all()
#         return queryset

#     def get_object(self):
#         """
#         Returns the object the view is displaying.

#         You may want to override this if you need to provide non-standard
#         queryset lookups.  Eg if objects are referenced using multiple
#         keyword arguments in the url conf.
#         """
#         queryset = self.filter_queryset(self.get_queryset())

#         # Perform the lookup filtering.
#         lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

#         assert lookup_url_kwarg in self.kwargs, (
#             'Expected view %s to be called with a URL keyword argument '
#             'named "%s". Fix your URL conf, or set the `.lookup_field` '
#             'attribute on the view correctly.' %
#             (self.__class__.__name__, lookup_url_kwarg)
#         )

#         filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
#         obj = get_object_or_404(queryset, **filter_kwargs)

#         # May raise a permission denied
#         self.check_object_permissions(self.request, obj)

#         return obj

#     def get_serializer(self, *args, **kwargs):
#         """
#         Return the serializer instance that should be used for validating and
#         deserializing input, and for serializing output.
#         """
#         serializer_class = self.get_serializer_class()
#         kwargs.setdefault('context', self.get_serializer_context())
#         return serializer_class(*args, **kwargs)

#     def get_serializer_class(self):
#         """
#         Return the class to use for the serializer.
#         Defaults to using `self.serializer_class`.

#         You may want to override this if you need to provide different
#         serializations depending on the incoming request.

#         (Eg. admins get full serialization, others get basic serialization)
#         """
#         assert self.serializer_class is not None, (
#             "'%s' should either include a `serializer_class` attribute, "
#             "or override the `get_serializer_class()` method."
#             % self.__class__.__name__
#         )

#         return self.serializer_class

#     def get_serializer_context(self):
#         """
#         Extra context provided to the serializer class.
#         """
#         return {
#             'request': self.request,
#             'format': self.format_kwarg,
#             'view': self
#         }

#     def filter_queryset(self, queryset):
#         """
#         Given a queryset, filter it with whichever filter backend is in use.

#         You are unlikely to want to override this method, although you may need
#         to call it either from a list view, or from a custom `get_object`
#         method if you want to apply the configured filtering backend to the
#         default queryset.
#         """
#         for backend in list(self.filter_backends):
#             queryset = backend().filter_queryset(self.request, queryset, self)
#         return queryset

#     @property
#     def paginator(self):
#         """
#         The paginator instance associated with the view, or `None`.
#         """
#         if not hasattr(self, '_paginator'):
#             if self.pagination_class is None:
#                 self._paginator = None
#             else:
#                 self._paginator = self.pagination_class()
#         return self._paginator

#     def paginate_queryset(self, queryset):
#         """
#         Return a single page of results, or `None` if pagination is disabled.
#         """
#         if self.paginator is None:
#             return None
#         return self.paginator.paginate_queryset(queryset, self.request, view=self)

#     def get_paginated_response(self, data):
#         """
#         Return a paginated style `Response` object for the given output data.
#         """
#         assert self.paginator is not None
#         return self.paginator.get_paginated_response(data)
        
# class GenericAPIView:
#     def get_queryset(self):
#         assert self.queryset is not None, (
#             "'%s' should either include a `queryset` attribute, "
#             "or override the `get_queryset()` method."
#             % self.__class__.__name__
#         )

#         queryset = self.queryset
#         if isinstance(queryset, QuerySet):
#             if self.request.query_params.get('filter') is not None:
#                 queryset = queryset.filter(**json.loads(self.request.query_params.get('filter')))
#             else:
#                 queryset = queryset.all()
#         return queryset

class RequestHandler(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    def get(self, request, pk=None):
        if pk is not None:
            return self.retrieve(request, pk)
        return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def patch(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)