-- lua/diagnostics.lua

vim.diagnostic.config({
  underline = true,
  virtual_text = false,
  severity_sort = true,
  float = {
    border = "rounded",
    source = "if_many",
  },
})
