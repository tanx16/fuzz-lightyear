import pytest

from fuzz_lightyear.datastore import _POST_FUZZ_HOOKS_BY_OPERATION
from fuzz_lightyear.datastore import _POST_FUZZ_HOOKS_BY_TAG
from fuzz_lightyear.datastore import get_excluded_operations
from fuzz_lightyear.datastore import get_included_tags
from fuzz_lightyear.datastore import get_non_vulnerable_operations
from fuzz_lightyear.datastore import get_user_defined_mapping
from fuzz_lightyear.plugins import get_enabled_plugins
from fuzz_lightyear.request import get_victim_session_factory
from fuzz_lightyear.supplements.abstraction import get_abstraction


@pytest.fixture(autouse=True)
def clear_caches():
    get_abstraction.cache_clear()
    get_user_defined_mapping.cache_clear()
    get_enabled_plugins.cache_clear()
    get_victim_session_factory.cache_clear()
    get_excluded_operations.cache_clear()
    get_non_vulnerable_operations.cache_clear()
    get_included_tags.cache_clear()

    _POST_FUZZ_HOOKS_BY_OPERATION.clear()
    _POST_FUZZ_HOOKS_BY_TAG.clear()
