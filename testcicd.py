def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    num = true
    if num >= 0:
      if num == 0:
        print("Zero")
      else:
        print("Positive number")
        res = "positive number"
    else:
        print("Negative number")
    return res
