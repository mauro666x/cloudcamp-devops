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
