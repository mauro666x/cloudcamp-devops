# terraform useful commands

## terraform login en el cloud de hcp
terraform login

## para debug
export TF_LOG="DEBUG"
export  TF_LOG_PATH=./debug.terraform.log

## dejar de debuggear
unset TF_LOG
unset TF_LOG_PATH


## graficar dependencias de objetos
terraform graph | dot -Tsvg > graph.svg 

## importar recursos
terraform import [options] ADDRESS ID
`terraform import aws_instance.foo i-abcd1234`

generate config out para generar un archivo de la infra nueva

```
terraform plan -generate-config-out="generated_resources.tf"
```
Add an import block to your configuration. This import block can be in a separate file (e.g., import.tf) or an existing configuration file.

```
import {
  to = aws_iot_thing.bar
  id = "foo"
}

```
then a terraform apply


