-- lua/lsp.lua

local lsp = vim.lsp

lsp.config.clangd = {
  cmd = {
    "clangd",
    "--offset-encoding=utf-16",
  },
  filetypes = { "c", "cpp", "objc", "objcpp" },
  root_dir = vim.fs.root(0, { ".git", "compile_commands.json", "build", "Makefile" }) or vim.fn.getcwd(),
}

lsp.config.lua_ls = {
  cmd = { "lua-language-server" },
  filetypes = { "lua" },
  root_dir = vim.fs.root(0, { ".git", "init.lua" }) or vim.fn.getcwd(),
  settings = {
    Lua = {
      diagnostics = {
        globals = { "vim" },
      },
    },
  },
}

lsp.config.pyright = {
  cmd = {
    "pyright-langserver",
    "--stdio",
  },
  filetypes = { "python" },
  root_dir = vim.fs.root(0, { ".git", "setup.py", "pyproject.toml", "requirements.txt" }) or vim.fn.getcwd(),
}

lsp.config.bashls = {
  cmd = {
    "bash-language-server",
    "start",
  },
  filetypes = { "sh", "bash", "zsh" },
  root_dir = vim.fs.root(0, { ".git", ".zshrc", ".bashrc" }) or vim.fn.getcwd(),
  settings = {
    bashIdiomSupport = true,
  },
}

lsp.enable("clangd")
lsp.enable("lua_ls")
lsp.enable("pyright")
lsp.enable("bashls")

vim.api.nvim_create_autocmd("LspAttach", {
  callback = function(ev)
    local client = lsp.get_client_by_id(ev.data.client_id)
    if client and client:supports_method('textDocument/completion') then
      vim.lsp.completion.enable(true, client.id)
    end

    vim.bo[ev.buf].omnifunc = "v:lua.vim.lsp.omnifunc"
  end,
})
