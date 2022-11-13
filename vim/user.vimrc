" 不与vi兼容
set nocompatible

" 打开语法高亮
syntax on

" 底部显示处于命令模式还是插入模式
set showmode

" 支持鼠标
set mouse=a

" 使用utf-8编码
set encoding=utf-8

" 显示行号
set number

" 光标所在当前行高亮
set cursorline

" 按下回车键下一行缩进与上一行缩进保持一致
set autoindent

" 一个制表符长度等于8个空格
set tabstop=8

" 缩进符自动转为空格
set expandtab

" 默认缩进8个空格大小
set shiftwidth=8

" 高亮搜索
set hlsearch

" 记住1000次历史操作
set history=1000

" 括号补全
inoremap ( ()<Esc>i
inoremap [ []<Esc>i
inoremap < <><Esc>i
inoremap { {}<Esc>i
inoremap ' ''<Esc>i
inoremap " ""<Esc>i

" 显示隐藏字符
set list

" 配置符号显示不可见字符
set listchars=tab:~~,space:·,extends:>,precedes:<
