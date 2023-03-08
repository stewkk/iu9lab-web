#!/usr/bin/env python3

import pathlib
import sys

import pytest

pytest_plugins = ['testsuite.pytest_plugin']


def pytest_addoption(parser):
    group = parser.getgroup('iu9lab service')
    group.addoption(
        '--iu9lab-service-port',
        help='Bind iu9lab service to this port (default is %(default)s)',
        default=8080,
        type=int,
    )


@pytest.fixture
async def iu9lab_service(
    ensure_daemon_started,
    # Service process holder
    iu9lab_service_scope,
    # Service dependencies
    mockserver,
):
    # Start service if not started yet
    await ensure_daemon_started(iu9lab_service_scope)


@pytest.fixture
async def iu9lab_client(
    create_service_client,
    iu9lab_service_baseurl,
    iu9lab_service,
):
    # Create service client instance
    return create_service_client(iu9lab_service_baseurl)


@pytest.fixture(scope='session')
def iu9lab_service_baseurl(pytestconfig):
    return f'http://localhost:{pytestconfig.option.iu9lab_service_port}/'


@pytest.fixture(scope='session')
def iu9lab_root():
    """Path to iu9lab service root."""
    return pathlib.Path(__file__).parent.parent


@pytest.fixture(scope='session')
async def iu9lab_service_scope(
    pytestconfig,
    create_daemon_scope,
    iu9lab_root,
    iu9lab_service_baseurl,
):
    async with create_daemon_scope(
        args=[
            str(iu9lab_root.joinpath('main')),
            '--port',
            str(pytestconfig.option.iu9lab_service_port),
        ],
        ping_url=iu9lab_service_baseurl + 'ping',
    ) as scope:
        yield scope
