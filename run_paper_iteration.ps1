param(
    [string]$Root = $PSScriptRoot
)

$ErrorActionPreference = "Stop"

$script = Join-Path -Path $Root -ChildPath "tools\paper_iteration.py"
if (-not (Test-Path -LiteralPath $script)) {
    throw "Cannot find paper iteration script at: $script"
}

$python = "C:\Users\Administrator\total-agent-memory\.venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) {
    $python = "py"
}

& $python $script --root $Root
