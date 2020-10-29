provider "aws" {
  region = "ap-northeast-1"
}

// TODO var.env 入れたい
data "aws_lambda_layer_version" "external_module_layer" {
  layer_name = "alexa-packages"
}

resource "aws_lambda_permission" "alexa_permission" {
  action = "lambda:InvokeFunction"
  function_name = "fgo_alexa_endpoint_${var.env}"
  principal = "alexa-appkit.amazon.com"
  event_source_token = var.event_source_token

  depends_on = [
    module.fgo_alexa_endpoint]
}

module "fgo_alexa_endpoint" {
  env = var.env
  source = "./modules/lambda"
  memory = 128
  description = ""
  environment = {
    "ASSETS_URL_PREFIX" = var.assets_url_prefix
    "BUCKET_REGION" = var.bucket_region
    "BUCKET_NAME" = var.bucket_name
  }
  external_module_layer_arn = data.aws_lambda_layer_version.external_module_layer.arn
  role = var.lambda_role
}
