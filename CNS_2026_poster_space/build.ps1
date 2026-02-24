param(
    [switch]$Clean
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if ($Clean) {
    if (Get-Command latexmk -ErrorAction SilentlyContinue) {
        & latexmk -C "main.tex"
        exit $LASTEXITCODE
    }
    Write-Error "latexmk not available."
    exit 1
}

$latexmkCommand = Get-Command latexmk -ErrorAction SilentlyContinue
if ($latexmkCommand) {
    & latexmk -pdf -synctex=1 -interaction=nonstopmode "main.tex"
    if ($LASTEXITCODE -eq 0) {
        exit 0
    }
    Write-Warning "latexmk failed; falling back to pdflatex."
}

& pdflatex -synctex=1 -interaction=nonstopmode "main.tex"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& pdflatex -synctex=1 -interaction=nonstopmode "main.tex"
exit $LASTEXITCODE

