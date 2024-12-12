
resource "aws_s3_bucket" "bucket_1" {
  bucket = "cloudcamp-terraform-mbenavides-12312df3"


  tags = {
    Name        = "cloudcamp-terraform-1"
    Environment = "Dev"
    team        = "cloud"
  }
}