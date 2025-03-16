-- lua select(3, require'nvim-treesitter'.statusline():find("class%s(%a+)"))
-- luaeval("select(3, require'nvim-treesitter'.statusline():find('class%s(%a+)'))")
--
-- map<C-M> <Cmd> 
--
-- call system('kitten @ send-text --match "title:ipythonn" "manim -q l ' . expand('%:t') . ' ' . luaeval([[select(3, require'nvim-treesitter'.statusline():find("class%s(%a+)"))]]) . '\r"')<CR>

--

M = {}

M.cmd = function(fname, cname)
  return {
    "kitten",
    "@",
    "send-text",
    "--match",
    [['title:ipythonn']],
    [['manim -q l ]] .. fname .. " " .. cname .. [[\r']],
  }
end

M.run_class = function()
  local cname = select(3, require("nvim-treesitter").statusline():find "class%s(%a+)")
  local fname = vim.fn.expand "%:t"
  local cmd = M.cmd(fname, cname)
  vim.fn.system(table.concat(cmd, " "))
end

vim.api.nvim_set_keymap("n", "<C-m>", [[<Cmd> lua require"hotkeys".run_class()<CR>]], { noremap = true, expr = true })

return M
