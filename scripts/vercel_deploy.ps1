# Simple Vercel deploy script for Windows PowerShell
param(
  [string]$Token = $env:VERCEL_TOKEN
)
if (-not $Token) {
  Write-Host "VERCEL_TOKEN not set. Aborting deploy." -ForegroundColor Yellow
  exit 1
}
npm i -g vercel
vercel --prod --token $Token
