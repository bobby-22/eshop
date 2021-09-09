git filter-branch --commit-filter "
                GIT_AUTHOR_EMAIL="<nlongn22@tuta.io>";
                git commit-tree "$@";
                git commit-tree "$@";
