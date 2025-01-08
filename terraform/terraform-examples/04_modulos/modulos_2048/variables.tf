variable "region" {
  description = "The region to deploy the resources into"
  default     = "us-east-1"
}

variable "cidr" {
  description = "The CIDR block for the VPC"
  default     = "10.10.0.0/24"
}
