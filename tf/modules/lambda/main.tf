data "archive_file" "fgo_handler_zip" {
  type = "zip"
  source_dir = "src"
  output_path = "fgo_alexa_endpoint.zip"
}

resource "aws_lambda_function" "fgo_handler" {
  filename = data.archive_file.fgo_handler_zip.output_path
  function_name = "fgo_alexa_endpoint_${var.env}"
  handler = "lambda_function.handler"
  role = var.role
  description = var.description
  layers = [var.external_module_layer_arn]
  memory_size = var.memory
  runtime = "python3.8"
  timeout = var.timeout
  reserved_concurrent_executions = var.reserved_concurrent_executions
  publish = true
  source_code_hash = data.archive_file.fgo_handler_zip.output_base64sha256
  environment {
    variables = var.environment
  }
  tags = {
    fgo = "lambda"
  }
}
