// main.tf

terraform {
  backend "s3" {
    bucket         = "mauricio-benavides-terraform-state"
    key            = "modulo-cloudcamp/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "cloudcamp-ddb-lock"
  }
}

module "example_module" {
  source       = "./mi_modulo"
}

output "ec2_id" {
  value = module.example_module.instance_id
}

output "ec2_ip" {
  value = module.example_module.ip
}