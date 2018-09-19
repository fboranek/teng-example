

#include "teng_utils.h"

std::string templ = R"__(
<html>
<?teng include file="common-head.html" ?>
    <body>
        <?teng frag row?><p>${rnum}
            <?teng frag col?>${cnum} <?teng endfrag?>
        </p><?teng endfrag?>
    </body>
</html>
)__";


int main(int argc, char* argv[])
{
    Teng::Teng_t teng("templates", Teng::Teng_t::LM_LOG_TO_OUTPUT);
    generate(teng, templ, *createFragment());
}
