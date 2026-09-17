vim.opt.hlsearch = true

vim.api.nvim_create_augroup("TemplateMake", { clear = true })
vim.lsp.config("zuban", {
	cmd = { vim.fn.getcwd() .. "/.venv/bin/zuban", "server" },
})

vim.api.nvim_create_autocmd("BufWritePost", {
	group = "TemplateMake",
	pattern = "main.py",
	command = "!make",
})

vim.cmd("only")
vim.cmd("edit input")
vim.cmd("vsplit main.py")
