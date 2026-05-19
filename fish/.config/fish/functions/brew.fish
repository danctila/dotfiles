function brew
    # Run the actual brew command
    command brew $argv

    # If the command was install/uninstall, update Brewfile and commit
    if contains -- $argv[1] install uninstall remove
        set -l dotfiles_path ~/Documents/GitHub/dotfiles

        # Only proceed if in a git repo and it's our dotfiles
        if test -d $dotfiles_path/.git
            cd $dotfiles_path

            # Update the Brewfile
            command brew bundle dump --file=Brewfile --force

            # Commit if there are changes
            if git diff --quiet Brewfile
                # No changes
                return
            end

            git add Brewfile
            git commit -m "Update Brewfile after brew $argv[1]"

            # Return to previous directory
            cd -
        end
    end
end
