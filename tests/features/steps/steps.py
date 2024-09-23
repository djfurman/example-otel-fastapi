import behave
from behave.api.async_step import async_run_until_complete
from httpx import ASGITransport, AsyncClient

from app.main import app

@behave.given("we are running an API")
def start_the_api(context) -> None:
    pass

@behave.when('we {method} the "{endpoint}" endpoint')
@async_run_until_complete()
async def make_an_api_call_to_method_and_endpoint(context, method: str, endpoint: str) -> None:
    context.method = method
    context.endpoint = endpoint

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        context.response = await ac.request(
            method=method,
            url=endpoint
        )


@behave.then("we should receive a {status_code:d} response")
def check_the_response_code(context, status_code: int) -> None:
    assert context.response.status_code == status_code


@behave.then('the response should contain "{key}"')
def check_the_response(context, key: str) -> None:
    assert key in context.response.json().keys()


@behave.then('the response key "{key}" should be {value}')
def check_a_response_key(context, key: str, value: str) -> None:
    if value.lower() == "true":
        test_value = True

    assert context.response.json().get(key) == test_value
