terraform {
  cloud {

    organization = "cloudcamp-labs"

    workspaces {
      name = "2048"
    }
  }
}

module "vpc" {
  source = "./modules/vpc"
  cidr = var.cidr
}

module "ec2" {
  source  = "./modules/ec2"
  vpc_id  = module.vpc.vpc_id
  subnet_id = module.vpc.public_subnet_id
  key_pair_name = "mauricio.benavides-key2"
}

