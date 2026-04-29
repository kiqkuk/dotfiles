-- lua/options.lua

local opt = vim.opt

opt.number = true
opt.relativenumber = true
opt.showmode = false

opt.expandtab = true
opt.shiftwidth = 2
opt.tabstop = 2

opt.termguicolors = true

opt.completeopt = { "menuone", "popup", "noinsert", "noselect" }
opt.autocomplete = true
opt.autocompletedelay = 100
opt.autocompletetimeout = 80

-- popup menu
opt.pumborder = "rounded"

opt.signcolumn = "yes"
opt.updatetime = 250

-- sane undo
opt.undofile = true

-- statusline
opt.statusline = "%!v:lua.require('statusline').render()"
