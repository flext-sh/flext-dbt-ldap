# FLEXT dbt LDAP

Projeto dbt para transformar dados LDAP em modelos analiticos operacionais e de auditoria.

Descricao oficial atual: "FLEXT dbt LDAP - dbt Models for LDAP Data Transformation".

## O que este projeto entrega

- Converte staging em marts com regras SQL versionadas.
- Padroniza transformacoes para identidades e grupos.
- Entrega camada analitica para consumo de BI e controles.

## Contexto operacional

- Entrada: tabelas de staging LDAP.
- Saida: modelos analiticos dbt para consulta.
- Dependencias: ambiente dbt e fonte LDAP previamente ingerida.

## Estado atual e risco de adocao

- Qualidade: **Alpha**
- Uso recomendado: **Nao produtivo**
- Nivel de estabilidade: em maturacao funcional e tecnica, sujeito a mudancas de contrato sem garantia de retrocompatibilidade.

## Diretriz para uso nesta fase

Aplicar este projeto somente em desenvolvimento, prova de conceito e homologacao controlada, com expectativa de ajustes frequentes ate maturidade de release.
