terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  # profile = "default"

}

resource "aws_instance" "terraform_instace" {
    ami = "ami-022e1a32d3f742bd8"
    instance_type = "t2.micro"

    tags = {
      Name = "Terraform_Instance"
    }
}

output "Terraform_ipaddress" {
  value = aws_instance.terraform_instace.public_ip
  
}