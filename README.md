## Introduction

Many vscode users use fonts like this with some themes that support italics, I want to do the same in vim. I've tried [FiraCodeiScript](https://github.com/kencrocken/FiraCodeiScript), [Operator Mono](https://www.typography.com/fonts/operator/styles) and [Dank Mono](https://dank.sh/) but their support for nerd font symbols is not very good.

Therefore, I decided to patch some fonts myself. All these fonts should support nerd font symbols and be suitable for use in TUI editors like vim.

Some fonts are free of charge, they are patched already and you can directly use the binary files. However, some fonts are not free, so you need to build them by yourself if you want to use them.

### Preview

For a preview of all available fonts, see [**this post**](https://www.sainnhe.dev/post/icursive-nerd-font-preview/).

## Installation

1. Clone this repository.
2. If you want to install non-free fonts, you need to buy the fonts and build them by yourself.
2. For linux users, follow this [guide](https://wiki.archlinux.org/index.php/Fonts#Manual_installation) to install them.

### Build

#### Op series

##### Requirements

1. Binary file of [Operator Mono](https://www.typography.com/fonts/operator/styles)
2. GNU Bash
3. Node.js
4. Python (v2.7+)
5. Python 2 (or Python 3), `python-fontforge` package. See [Nerd Font Patcher](https://github.com/ryanoasis/nerd-fonts/#font-patcher) for details.
6. [`fonttools`](https://github.com/fonttools/fonttools) package. See [Operator Mono Ligatures](https://github.com/kiliman/operator-mono-lig#prerequisites) for details.

##### Steps

1. Clone this repository.
2. `cd /path/to/icursive-nerd-font` and execute `./build.sh Op /absolute/path/to/OperatorMono-BookItalic.otf`

E.g.:

```sh
./build.sh Op /home/sainnhe/Downloads/Operator\ Mono/Operator\ Mono\ Book\ Italic.otf
```

The new font files will be placed in the `*Op` folders.

#### Dk series

##### Requirements

1. Binary file of [Dank Mono](https://dank.sh)
2. GNU Bash
3. Python (v2.7+)
4. Python 2 (or Python 3), `python-fontforge` package. See [Nerd Font Patcher](https://github.com/ryanoasis/nerd-fonts/#font-patcher) for details.

##### Steps

1. Clone this repository.
2. `cd /path/to/icursive-nerd-font` and execute `./build.sh Dk /absolute/path/to/Dank\ Mono\ Italic.ttf`

E.g.:

```sh
./build.sh Dk /home/sainnhe/Downloads/Dank\ Mono\ Italic.ttf
```

The new font files will be placed in the `*Dk` folders.

#### Cg series

##### Requirements

1. Binary file of [Cartograph](https://connary.com/cartograph.html)
2. GNU Bash
3. Python (v2.7+)
4. Python 2 (or Python 3), `python-fontforge` package. See [Nerd Font Patcher](https://github.com/ryanoasis/nerd-fonts/#font-patcher) for details.

##### Steps

1. Clone this repository.
2. `cd /path/to/icursive-nerd-font` and execute `./build.sh Cg /absolute/path/to/Cartograph\ CF\ Italic.ttf`

E.g.:

```sh
./build.sh Dk /home/sainnhe/Downloads/Cartograph\ CF\ Italic.ttf
```

The new font files will be placed in the `*Cg` folders.

## Contributing

See [PATCH.md](./PATCH.md) for more information.

## FAQ

**Q: What's the color scheme used here?**

**A:** [Gruvbox Material](https://github.com/sainnhe/gruvbox-material) using `mix` palette.

**Q: What's your status line configuration?**

**A:** See this [article](https://www.sainnhe.dev/post/status-line-config/).

## Inspiration

[kencrocken/FiraCodeiScript](https://github.com/kencrocken/FiraCodeiScript)
