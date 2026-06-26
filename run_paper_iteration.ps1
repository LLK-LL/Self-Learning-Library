param(
    [string]$Root = $PSScriptRoot
)

$ErrorActionPreference = "Stop"

$script = Join-Path -Path $Root -ChildPath "tools\paper_iteration.py"
if (-not (Test-Path -LiteralPath $script)) {
    throw "Cannot find paper iteration script at: $script"
}

$python = if ($env:SELF_LEARNING_LIBRARY_PYTHON) {
    $env:SELF_LEARNING_LIBRARY_PYTHON
} else {
    "py"
}

& $python $script --root $Root
