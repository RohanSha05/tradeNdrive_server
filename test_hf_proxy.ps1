# Test HF proxy endpoint
# Usage: Set HF_TOKEN env var, then run this script

$model = "google/flan-t5-small"
$url = "http://127.0.0.1:8000/api/hf/$model"
$payload = @{
    inputs = "Translate English to French: How are you?"
} | ConvertTo-Json

Write-Host "Testing proxy: POST $url"
Write-Host "Payload: $payload"
Write-Host "HF_TOKEN set: $(if ([Environment]::GetEnvironmentVariable('HF_TOKEN')) { 'YES' } else { 'NO' })"
Write-Host ""

try {
    $response = Invoke-WebRequest -Uri $url `
        -Method POST `
        -Body $payload `
        -ContentType "application/json" `
        -ErrorAction Continue
    
    Write-Host "Status: $($response.StatusCode)"
    Write-Host "Response:"
    Write-Host $response.Content
} catch {
    Write-Host "Error: $($_.Exception.Message)"
    Write-Host "Response:"
    if ($_.Exception.Response) {
        Write-Host $_.Exception.Response.StatusCode
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        Write-Host $reader.ReadToEnd()
    }
}
