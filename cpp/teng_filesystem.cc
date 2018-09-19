#include "teng_utils.h"

std::string templ = R"__(
<html>
<?teng include file="in-memmory-common-head.html" ?>
    <body>
        <?teng frag row?><p>${rnum}
            <?teng frag col?>${cnum} <?teng endfrag?>
        </p><?teng endfrag?>
    </body>
</html>
)__";

std::string head = R"__(    <head>
        <title>Example page: ${title}</title>
    </head>
)__";


int main(int argc, char* argv[])
{
    auto* fs = new Teng::InMemoryFilesystem_t();
    fs->storage.insert(std::make_pair("in-memmory-common-head.html", head));
    Teng::Teng_t teng(fs, 0);
    generate(teng, templ, *createFragment());
}