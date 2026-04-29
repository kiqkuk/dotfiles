-- lua/plugins/colors.lua

require("catppuccin").setup({
  flavour = "mocha",
  transparent_background = true,
  term_colors = true,

  styles = {
    comments = { "italic" },
    conditionals = {},
    loops = {},
    functions = {},
    keywords = {},
    strings = {},
    variables = {},
  },

  integrations = {

  },
})

vim.cmd.colorscheme("catppuccin-mocha")

local cp = require("catppuccin.palettes").get_palette("mocha")
local set_hl = vim.api.nvim_set_hl

-- mode colors
set_hl(0, "StatusNormal", { fg = cp.crust, bg = cp.lavender, bold = true })
set_hl(0, "StatusInsert", { fg = cp.crust, bg = cp.green, bold = true })
set_hl(0, "StatusVisual", { fg = cp.crust, bg = cp.peach, bold = true })
set_hl(0, "StatusReplace", { fg = cp.crust, bg = cp.red, bold = true })
set_hl(0, "StatusCmd", { fg = cp.crust, bg = cp.yellow, bold = true })
set_hl(0, "StatusTerminal", { fg = cp.crust, bg = cp.flamingo, bold = true })

-- other colors
set_hl(0, "StatusFile", { fg = cp.lavender, bg = cp.base, bold = true })
set_hl(0, "StatusDir", { fg = cp.overlay0, bg = cp.base })
set_hl(0, "StatusMod", { fg = cp.text, bg = cp.base })
set_hl(0, "StatusRO", { fg = cp.red, bg = cp.base })
set_hl(0, "StatusDiag", { fg = cp.text, bg = cp.base })
set_hl(0, "StatusFt", { fg = cp.peach, bg = cp.base, bold = true })
set_hl(0, "StatusPos", { fg = cp.overlay0, bg = cp.base, bold = true })
