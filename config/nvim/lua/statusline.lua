-- lua/statusline.lua

local M = {}

local mode_map = {
  ['n']   = { 'NORMAL',   '%#StatusNormal#' },
  ['i']   = { 'INSERT',   '%#StatusInsert#' },
  ['v']   = { 'VISUAL',   '%#StatusVisual#' },
  ['V']   = { 'V-LINE',   '%#StatusVisual#' },
  ['\22'] = { 'V-BLOCK',  '%#StatusVisual#' },
  ['c']   = { 'COMMAND',  '%#StatusCmd#' },
  ['R']   = { 'REPLACE',  '%#StatusReplace#' },
  ['t']   = { 'TERM',     '%#StatusTerminal#' },
}

function M.render()
  local mode_data = mode_map[vim.api.nvim_get_mode().mode] or { 'UNKNOWN', '%#StatusNormal#' }
  local label = mode_data[1]
  local highlight = mode_data[2]

  local mode_str = string.format("%s %s ", highlight, label)

  local file_str = "%#StatusFile# %t "

  local dir = vim.fn.expand("%:~:h")
  if dir == "." then dir = "~" end
  local dir_str = string.format("%%#StatusDir# %s/ ", dir)

  local mod_str = "%#StatusMod#%m "
  local ro_str = "%#StatusRO#%r "

  local diag = vim.diagnostic.status()
  local diag_str = (diag and diag ~= "") and ("%#StatusDiag# " .. diag .. " ") or ""

  local ft = vim.bo.filetype:upper()
  local ft_str = string.format("%%#StatusFt# %s ", ft )

  local location = "%l:%c"
  local position = "%P"
  local pos_str = string.format("%%#StatusPos# [%s] %s ", location, position)

  return table.concat({
    mode_str,
    file_str,
    dir_str,
    mod_str,
    ro_str,
    "%=",
    diag_str,
    ft_str,
    pos_str
  })
end

return M
