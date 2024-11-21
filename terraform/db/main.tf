terraform {
  required_providers {
    mongodbatlas = {
      source  = "mongodb/mongodbatlas"
      version = "1.12.0" # Certifique-se de usar a versão mais recente
    }
  }
}

provider "mongodbatlas" {
  public_key  = var.atlas_public_key
  private_key = var.atlas_private_key
}

# Criar um projeto no MongoDB Atlas
resource "mongodbatlas_project" "project" {
  name   = var.project_name
  org_id = var.org_id
}

# Criar um cluster M0 (Free Tier)
resource "mongodbatlas_cluster" "cluster" {
  project_id                   = mongodbatlas_project.project.id
  name                         = "MeuClusterM0"
  cluster_type                 = "REPLICASET"     # Para M0, use "REPLICASET"
  provider_name                = "TENANT"         # Para M0, use "TENANT"
  provider_instance_size_name  = "M0"             # Opções: M0 (grátis), M2, M5
  provider_region_name         = "US_EAST_1"      # Região desejada
  backing_provider_name        = "AWS"            # Provedor de nuvem subjacente
  auto_scaling_disk_gb_enabled = true             # Habilitar auto scaling de disco
}

# Configurar a lista de acesso por IP
resource "mongodbatlas_project_ip_access_list" "access_list" {
  project_id = mongodbatlas_project.project.id

  cidr_block = "0.0.0.0/0" # Acesso aberto (não recomendado para produção)
  comment    = "Acesso aberto para testes"
}

# Criar um usuário de banco de dados
resource "mongodbatlas_database_user" "db_user" {
  username           = "$MONGOUSER"
  password           = "$MONGOPASSOWD"
  auth_database_name = "admin"
  project_id         = mongodbatlas_project.project.id

  roles {
    role_name     = "readWriteAnyDatabase"
    database_name = "admin"
  }
}

