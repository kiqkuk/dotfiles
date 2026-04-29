-- lua/treesitter.lua

local ts = vim.treesitter

vim.api.nvim_create_autocmd("FileType", {
  callback = function(ev)
    local lang = ts.language.get_lang(vim.bo[ev.buf].filetype)
    if lang and pcall(ts.language.add, lang) then
      pcall(ts.start, ev.buf, lang)
    end
  end,
})
