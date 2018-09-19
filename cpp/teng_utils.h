#include <assert.h>
#include <memory>
#include <stdio.h>
#include <string>
#include <teng.h>
#include <tengfilesystem.h>

inline auto createFragment()
{
    // Root data fragment
    auto root = std::make_unique<Teng::Fragment_t>();

    // Rows fragment list
    auto& rowList = root->addFragmentList("row");

    // Create rows
    for (const auto& value : {"A", "B"}) {
        auto& row = rowList.addFragment();
        row.addVariable("rnum", value);
        // Create columns
        for (int j = 1; j <= 2; ++j) {
            auto& col = row.addFragment("col");
            col.addVariable("cnum", static_cast<Teng::IntType_t>(j));
        }
    }
    return root;
}

inline void generate(Teng::Teng_t& teng, const std::string& templ, const Teng::Fragment_t& root)
{
    // Output to standard output
    Teng::FileWriter_t writer(stdout);

    // Simple error log
    Teng::Error_t err;

    // Generate page
    bool res = teng.generatePage(templ,       // Template
                                 "",          // Dictionary (none)
                                 "",          // Language (none)
                                 "",          // Configuration (none)
                                 "text/html", // Content type
                                 "utf-8",     // Encoding
                                 root,        // Root fragment
                                 writer,      // Writer
                                 err          // Error log
                                 )
        == 0;

    if (!res) {
        err.dump(std::cerr);
        std::runtime_error("Failed to generate page.");
    }
}
