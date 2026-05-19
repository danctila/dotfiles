# dotfiles

Personal configuration files and setup for macOS development environment.

## Contents

- **Brewfile** - Homebrew packages, CLI tools, applications, and VS Code extensions
- **install.sh** - Installation script to bootstrap packages from Brewfile
- **fish/** - Fish shell configuration
- **git/** - Git configuration
- **kitty/** - Kitty terminal emulator theme and settings
- **lazygit/** - Lazy Git configuration
- **zellij/** - Zellij terminal multiplexer configuration

## Installation

Clone the repository and run the install script to install all packages:

```bash
git clone https://github.com/danctila/dotfiles.git
cd dotfiles
./install.sh
```

To link specific configuration files, use [GNU Stow](https://www.gnu.org/software/stow/):

```bash
# Link all configs
stow fish git kitty lazygit zellij

# Or link specific packages
stow fish
stow kitty
```

Stow will create symlinks in your home directory (`~/.config/`) pointing to the config files in this repository.

## Tools

This repository manages configuration for:

- **[Fish](https://fishshell.com/)** - User-friendly shell
- **[Git](https://git-scm.com/)** - Version control
- **[Kitty](https://sw.kovidgoyal.net/kitty/)** - GPU-based terminal emulator
- **[Lazy Git](https://github.com/jesseduffield/lazygit)** - Git terminal UI
- **[Zellij](https://zellij.dev/)** - Terminal multiplexer

## Development Tools

The Brewfile includes development tools for:

- Go, Python, Node.js, Ruby, Rust, and more
- Databases: MongoDB, PostgreSQL, Redis
- Cloud: AWS CLI, Cloudflare, Supabase, Temporal
- Development: Neovim, Git Delta, ast-grep, ripgrep, fzf
- VS Code extensions for development across multiple languages and frameworks

## Notes

- Modify Brewfile to customize installed packages
- Configuration files use standard formats (TOML, KDL, YAML)
- Git LFS is configured in `.gitconfig`
- Starship prompt is configured in Fish shell
