from drf_spectacular.utils import OpenApiResponse, extend_schema


# Responseの繰り返しはたしかにうるさい
# Viewはもはやベタガキでもいい気がしてきた。
# -> getとかすると ~~ | Anyになるのは気持ち悪い。 やはりスコープを小さくするべきか
# -> serializer.dataもAny,,,
def handle_request(tags=[]):
  def _handle_request(req=None, res=None, params=[]):
    def _decorator(function):
      def _wrap(self, request, *args, **kwargs):
        return function(self, request, *args, **kwargs)
      return extend_schema(
        # description=description,
        # summary="Create new Summary",
        parameters=params,
        request=req,
        responses={
          200: OpenApiResponse(
            response=res,
          ),
          201: OpenApiResponse(
            response=res,
          ),
          400: OpenApiResponse(
            description="Bad Request",
          ),
          500: OpenApiResponse(
            description="Internal Server Error"   
          ),
        },
        tags=tags
      )(_wrap)
    return _decorator
  return _handle_request