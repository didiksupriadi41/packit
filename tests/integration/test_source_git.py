from tests.utils import get_specfile
from packit.utils import cwd
    spec_package_section = ""
    for section in spec.spec_content.sections:
        if "%package" in section[0]:
            spec_package_section += "\n".join(section[1])
    spec_package_section = ""
    for section in spec.spec_content.sections:
        if "%package" in section[0]:
            spec_package_section += "\n".join(section[1])