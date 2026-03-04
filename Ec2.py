# Create EC2 Instance
resource "aws_instance" "my_ec2" {
  ami                         = "ami-0c02fb55956c7d316"  # Amazon Linux 2 (us-east-1)
  instance_type               = "t3.micro"
  subnet_id                   = aws_subnet.my_subnet.id
  vpc_security_group_ids      = [aws_security_group.my_sg.id]
  associate_public_ip_address = true
#tags are here

  tags = {
    Name = "rachita-terraform-ec2"
    cost ="Sales"
  }
key_name = "rachita-key02"
user_data = <<-EOF
