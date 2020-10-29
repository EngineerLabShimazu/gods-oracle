variable "env" {}
variable "description" {}
variable "external_module_layer_arn" {}
variable "memory" {
  default = 128
}
variable "timeout" {
  default = 300
}
variable "reserved_concurrent_executions" {
  default = -1
}
variable "role" {}
variable "environment" {}