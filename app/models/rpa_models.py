from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, 
                        Integer, String, ForeignKey)

from datetime import datetime

metadata_obj = MetaData()


schedulers = Table(
    "schedulers",
    metadata_obj,
    Column("cod_scheduler", Integer, primary_key=True),
    Column("data", datetime, nullable=False),
    Column("dia", Integer),
    Column("mes", Integer, nullable=False),
    Column("status", String(50), nullable=False),
    Column("falha", String(50), nullable=False),
    Column("tempo", Integer, nullable=False),
    Column("funcaopython", String(50), nullable=False),
    schema="RPA"
)

usuarioRpa = Table(
    "usuario_rpa",
    metadata_obj,
    Column("cod_usuario", Integer, primary_key=True),
    Column("nome", String(16), nullable=False),
    Column("email", String(60)),
    Column("data_cadastro", datetime, nullable=False),
    Column("data_atualizacao", datetime, nullable=False),
    Column("cod_scheduler", Integer, ForeignKey("schedulers.cod_scheduler")),
    schema="RPA"
)


checagem = Table(
    "checagem",
    metadata_obj,
    Column("cod_checagem", Integer, primary_key=True),
    Column("data", datetime, nullable=False),
    Column("erro", String(200),
    Column("descricao", String(600),
    Column("data_atualizado", datetime),
    Column("status", String(20)),
    Column("cod_scheduler", Integer, ForeignKey("schedulers.cod_scheduler")),
    schema="RPA"))


captcha = Table(
    "captcha",
    metadata_obj,
    Column("cod_captcha", Integer, primary_key=True),
    Column("data", String(16), nullable=False),
    Column("path", String(60)),
    Column("erro", boolean),
    Column("retorno", boolean),
    Column("cod_scheduler", Integer, ForeignKey("schedulers.cod_scheduler")),
    schema="RPA"
)
