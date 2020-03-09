# This is an auto-generated Django model module. You'll have to do the
# following manually to clean this up: * Rearrange models' order * Make sure
# each model has one field with primary_key=True * Make sure each ForeignKey
# and OneToOneField has `on_delete` set to the desired behavior * Remove
# `managed = False` lines if you wish to allow Django to create, modify,
# and delete the table Feel free to rename the models, but don't rename
# db_table values or field names.
from django.db import models


class AtividadesPrincipais(models.Model):
    atp_codigo = models.AutoField(primary_key=True)
    atp_nome = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'atividades_principais'


class Clientes(models.Model):
    cli_codigo = models.AutoField(primary_key=True)
    neg_codigo = models.PositiveIntegerField(blank=True, null=True)
    cli_nomefantasia_nomecomercial = models.CharField(max_length=100,
                                                      blank=True, null=True)
    cli_razaosocial_nomecompleto = models.CharField(max_length=60, blank=True,
                                                    null=True)
    cli_tipopessoa = models.CharField(max_length=1, blank=True, null=True)
    cli_cpf_cnpj = models.CharField(max_length=20, blank=True, null=True)
    cli_rg_ie = models.CharField(max_length=20, blank=True, null=True)
    cli_tel_ddd = models.CharField(max_length=3, blank=True, null=True)
    cli_tel_ramal = models.CharField(max_length=10, blank=True, null=True)
    cli_tel = models.CharField(max_length=10, blank=True, null=True)
    cli_fax_ddd = models.CharField(max_length=3, blank=True, null=True)
    cli_fax_ramal = models.CharField(max_length=10, blank=True, null=True)
    cli_fax = models.CharField(max_length=10, blank=True, null=True)
    cli_valorminimo = models.CharField(max_length=20, blank=True, null=True)
    cli_site = models.CharField(max_length=60, blank=True, null=True)
    cli_preferencial = models.CharField(max_length=1, blank=True, null=True)
    cli_atividade = models.CharField(max_length=45, blank=True, null=True)
    cli_ativo = models.CharField(max_length=1, blank=True, null=True)
    cli_coef_prova = models.CharField(max_length=20, blank=True, null=True)
    cli_coef_fotolito = models.CharField(max_length=20, blank=True, null=True)
    cli_pendenciafinan = models.CharField(max_length=45, blank=True, null=True)
    cli_chapa = models.CharField(max_length=45, blank=True, null=True)
    cli_os_correcao = models.CharField(max_length=1, blank=True, null=True)
    cli_descricao = models.TextField(blank=True, null=True)

    def full_fone(self):
        return f"({self.cli_tel_ddd}) {self.cli_tel[:4]}-{self.cli_tel[-4:]}"

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class ClientesContatos(models.Model):
    cnt_codigo = models.AutoField(primary_key=True)
    cli_codigo = models.PositiveIntegerField()
    cnt_nome = models.CharField(max_length=60, blank=True, null=True)
    cnt_tel_ddd = models.CharField(max_length=3, blank=True, null=True)
    cnt_telefone = models.CharField(max_length=10, blank=True, null=True)
    cnt_tel_ramal = models.CharField(max_length=10, blank=True, null=True)
    cnt_cel_ddd = models.CharField(max_length=3, blank=True, null=True)
    cnt_celular = models.CharField(max_length=10, blank=True, null=True)
    cnt_email = models.CharField(max_length=60, blank=True, null=True)
    cnt_setor = models.CharField(max_length=100, blank=True, null=True)
    cnt_responsavel = models.CharField(max_length=1, blank=True, null=True)
    cnt_idnextel = models.CharField(max_length=50, blank=True, null=True)

    def full_fone(self):
        return f"({self.cnt_tel_ddd}) " \
               f"{self.cnt_telefone[:4]}-{self.cnt_telefone[-4:]}"

    def full_mobile(self):
        return f"({self.cnt_cel_ddd}) {self.cnt_celular}"

    class Meta:
        managed = False
        db_table = 'clientes_contatos'


class ClientesFormatosChapa(models.Model):
    cli_codigo = models.PositiveIntegerField()
    fcp_codigo = models.PositiveIntegerField(primary_key=True)
    cfc_utiliza = models.CharField(max_length=1, blank=True, null=True)
    cfc_pinca = models.CharField(max_length=20, blank=True, null=True)
    cfc_coef = models.CharField(max_length=20, blank=True, null=True)
    cfc_expessura = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_formatos_chapa'
        unique_together = (('fcp_codigo', 'cli_codigo'),)


class ClientesFormatosProva(models.Model):
    cli_codigo = models.PositiveIntegerField(primary_key=True)
    fpr_codigo = models.PositiveIntegerField()
    cfp_valor = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_formatos_prova'
        unique_together = (('cli_codigo', 'fpr_codigo'),)


class ClientesServicosUtilizados(models.Model):
    cli_codigo = models.PositiveIntegerField(primary_key=True)
    srv_codigo = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'clientes_servicos_utilizados'
        unique_together = (('cli_codigo', 'srv_codigo'),)


class Cores(models.Model):
    cor_valor = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'cores'


class Enderecos(models.Model):
    end_codigo = models.AutoField(primary_key=True)
    cli_codigo = models.PositiveIntegerField()
    end_descricao = models.CharField(max_length=45, blank=True, null=True)
    end_tipo = models.CharField(max_length=45, blank=True, null=True)
    end_logradouro = models.CharField(max_length=60, blank=True, null=True)
    end_numero = models.CharField(max_length=10, blank=True, null=True)
    end_complemento = models.CharField(max_length=40, blank=True, null=True)
    end_bairro = models.CharField(max_length=45, blank=True, null=True)
    end_zona = models.CharField(max_length=45, blank=True, null=True)
    end_cep = models.CharField(max_length=9, blank=True, null=True)
    end_cidade = models.CharField(max_length=45, blank=True, null=True)
    end_estado = models.CharField(max_length=40, blank=True, null=True)
    end_referencia = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enderecos'


class FormatosChapa(models.Model):
    fcp_codigo = models.AutoField(primary_key=True)
    fcp_formato = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'formatos_chapa'


class FormatosProva(models.Model):
    fpr_codigo = models.AutoField(primary_key=True)
    fpr_papel = models.CharField(max_length=20, blank=True, null=True)
    fpr_valor = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formatos_prova'


class HorariosEntrega(models.Model):
    hor_codigo = models.AutoField(primary_key=True)
    hor_horario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'horarios_entrega'


class Lineatura(models.Model):
    lin_valor = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'lineatura'


class Mensagens(models.Model):
    msg_codigo = models.AutoField(primary_key=True)
    msg_texto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagens'


class MensagensOpcoes(models.Model):
    mop_codigo = models.AutoField(primary_key=True)
    mop_texto = models.CharField(max_length=255, blank=True, null=True)
    msg_codigo = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagens_opcoes'


class Negociacao(models.Model):
    neg_codigo = models.AutoField(primary_key=True)
    neg_nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'negociacao'


class Os(models.Model):
    os_codigo = models.AutoField(primary_key=True)
    cli_codigo = models.PositiveIntegerField()
    os_dataabertura = models.DateField()
    os_dataprometida = models.DateField()
    os_hora = models.TimeField()
    up_codigo2 = models.CharField(max_length=15, blank=True, null=True)
    usu_login = models.CharField(max_length=100, blank=True, null=True)
    hor_codigo = models.PositiveIntegerField(blank=True, null=True)
    neg_codigo = models.CharField(max_length=60, blank=True, null=True)
    os_status = models.CharField(max_length=1, blank=True, null=True)
    os_correcao = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os'
        unique_together = (('os_codigo', 'cli_codigo'),)
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de serviço'


class OsArquivos(models.Model):
    arq_codigo = models.AutoField(primary_key=True)
    arq_nome = models.CharField(max_length=60)
    arq_envio = models.CharField(max_length=20, blank=True, null=True)
    arq_tipo = models.CharField(max_length=60, blank=True, null=True)
    arq_programa = models.CharField(max_length=50, blank=True, null=True)
    arq_plataforma = models.CharField(max_length=40, blank=True, null=True)
    arq_print = models.CharField(max_length=35, blank=True, null=True)
    os_codigo = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_arquivos'


class OsConfirmacao(models.Model):
    com_codigo = models.AutoField(primary_key=True)
    cli_codigo = models.PositiveIntegerField()
    os_codigo = models.PositiveIntegerField()
    msg_codigo = models.PositiveIntegerField(blank=True, null=True)
    com_observacaoaprovacao = models.TextField(blank=True, null=True)
    com_endereco = models.TextField(blank=True, null=True)
    com_retirarestudio_entregar = models.CharField(max_length=1, blank=True,
                                                   null=True)
    com_entregaurgente = models.CharField(max_length=1, blank=True, null=True)
    com_data = models.DateField(blank=True, null=True)
    hor_codigo = models.IntegerField(blank=True, null=True)
    com_observacaoentrega = models.TextField(blank=True, null=True)
    up_codigo = models.CharField(max_length=15, blank=True, null=True)
    com_negociacao = models.CharField(max_length=60, blank=True, null=True)
    com_fotolito = models.FloatField(blank=True, null=True)
    com_provas = models.FloatField(blank=True, null=True)
    com_ctp = models.FloatField(blank=True, null=True)
    com_plusservice = models.FloatField(blank=True, null=True)
    com_total = models.FloatField(blank=True, null=True)
    com_retirarestudio = models.CharField(max_length=1, blank=True, null=True)
    end_codigo = models.PositiveIntegerField(blank=True, null=True)
    mop_codigo = models.PositiveIntegerField(blank=True, null=True)
    com_contato = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_confirmacao'
        unique_together = (('com_codigo', 'cli_codigo', 'os_codigo'),)


class OsCorrecao(models.Model):
    osc_codigo = models.AutoField(primary_key=True)
    os_codigo = models.IntegerField()
    cli_codigo = models.PositiveIntegerField()
    osc_tec_platesetter = models.CharField(max_length=1, blank=True, null=True)
    osc_tec_apogeex = models.CharField(max_length=1, blank=True, null=True)
    osc_tec_aplicacao = models.CharField(max_length=1, blank=True, null=True)
    osc_tec_outro = models.CharField(max_length=1, blank=True, null=True)
    osc_tec_processadora = models.CharField(max_length=1, blank=True,
                                            null=True)
    osc_pro_fechamento = models.CharField(max_length=1, blank=True, null=True)
    osc_pro_tracado = models.CharField(max_length=1, blank=True, null=True)
    osc_pro_imagem = models.CharField(max_length=1, blank=True, null=True)
    osc_pro_fonte = models.CharField(max_length=1, blank=True, null=True)
    osc_pro_outro = models.CharField(max_length=100, blank=True, null=True)
    osc_responsavel = models.CharField(max_length=100, blank=True, null=True)
    osc_ocorrencia = models.TextField(blank=True, null=True)
    osc_natureza = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_correcao'


class OsCtp(models.Model):
    ctp_codigo = models.AutoField(primary_key=True)
    imp_codigo = models.PositiveIntegerField()
    ctp_quantidade = models.PositiveIntegerField(blank=True, null=True)
    ctp_formatoschapa = models.PositiveIntegerField(blank=True, null=True)
    ctp_pinca = models.FloatField(blank=True, null=True)
    ctp_valor = models.FloatField(blank=True, null=True)
    ctp_forneada = models.CharField(max_length=15, blank=True, null=True)
    ctp_lineatura = models.IntegerField(blank=True, null=True)
    ctp_reticula = models.CharField(max_length=45, blank=True, null=True)
    os_codigo = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_ctp'


class OsFotolito(models.Model):
    fot_codigo = models.AutoField(primary_key=True)
    imp_codigo = models.PositiveIntegerField()
    fot_quantidade = models.PositiveIntegerField(blank=True, null=True)
    fot_cor = models.CharField(max_length=3, blank=True, null=True)
    fot_largura = models.CharField(max_length=15, blank=True, null=True)
    fot_altura = models.FloatField(blank=True, null=True)
    fot_valor = models.FloatField(blank=True, null=True)
    os_codigo = models.PositiveIntegerField(blank=True, null=True)
    fot_objetivo = models.CharField(max_length=50, blank=True, null=True)
    fot_lineatura = models.IntegerField(blank=True, null=True)
    fot_filme = models.CharField(max_length=50, blank=True, null=True)
    fot_impressao = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_fotolito'


class OsImpressos(models.Model):
    imp_codigo = models.AutoField(primary_key=True)
    os_codigo = models.PositiveIntegerField()
    cli_codigo = models.PositiveIntegerField()
    arq_codigo = models.PositiveIntegerField()
    imp_titulo = models.CharField(max_length=60, blank=True, null=True)
    imp_tipomontagem = models.CharField(max_length=1, blank=True, null=True)
    imp_tipo_promo = models.CharField(max_length=1, blank=True, null=True)
    imp_paginas_promo = models.CharField(max_length=50, blank=True, null=True)
    imp_formato_promo = models.CharField(max_length=50, blank=True, null=True)
    imp_cores_promo = models.CharField(max_length=50, blank=True, null=True)
    imp_acabamento_promo = models.CharField(max_length=50, blank=True,
                                            null=True)
    imp_montagemtipo_promo = models.CharField(max_length=50, blank=True,
                                              null=True)
    imp_figurarfolha_promo = models.CharField(max_length=50, blank=True,
                                              null=True)
    imp_posicaofolha_promo = models.CharField(max_length=50, blank=True,
                                              null=True)
    imp_corte_promo = models.CharField(max_length=50, blank=True, null=True)
    imp_aberturavertical_promo = models.CharField(max_length=50, blank=True,
                                                  null=True)
    imp_aberturahorizontal_promo = models.CharField(max_length=50, blank=True,
                                                    null=True)
    imp_observacao_promo = models.CharField(max_length=150, blank=True,
                                            null=True)
    imp_tipo_edit = models.CharField(max_length=50, blank=True, null=True)
    imp_montagem_edit = models.CharField(max_length=50, blank=True, null=True)
    imp_paginas_edit = models.CharField(max_length=50, blank=True, null=True)
    imp_formato_edit = models.CharField(max_length=50, blank=True, null=True)
    imp_cores_edit = models.CharField(max_length=50, blank=True, null=True)
    imp_orientacaopagina = models.CharField(max_length=20, blank=True,
                                            null=True)
    imp_infomontagem = models.CharField(max_length=50, blank=True, null=True)
    imp_figurasfolha_edit = models.CharField(max_length=50, blank=True,
                                             null=True)
    imp_numeropaginas_edit = models.CharField(max_length=50, blank=True,
                                              null=True)
    imp_posicaofolha_edit = models.CharField(max_length=50, blank=True,
                                             null=True)
    imp_corte_edit = models.CharField(max_length=50, blank=True, null=True)
    imp_aberturavertical_edit = models.CharField(max_length=50, blank=True,
                                                 null=True)
    imp_aberturahorizontal_edit = models.CharField(max_length=50, blank=True,
                                                   null=True)
    imp_observacao_edit = models.CharField(max_length=150, blank=True,
                                           null=True)

    class Meta:
        managed = False
        db_table = 'os_impressos'


class OsLog(models.Model):
    log_codigo = models.AutoField(primary_key=True)
    os_codigo = models.PositiveIntegerField()
    sts_status = models.CharField(max_length=1, blank=True, null=True)
    log_datahora = models.DateTimeField(blank=True, null=True)
    usu_login = models.CharField(max_length=60, blank=True, null=True)
    log_observacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_log'


class OsPlusService(models.Model):
    plus_codigo = models.AutoField(primary_key=True)
    cli_codigo = models.PositiveIntegerField()
    os_codigo = models.PositiveIntegerField()
    plus_diagramacao = models.CharField(max_length=1, blank=True, null=True)
    plus_fechamento = models.CharField(max_length=1, blank=True, null=True)
    plus_scanner = models.CharField(max_length=1, blank=True, null=True)
    plus_perfil = models.CharField(max_length=1, blank=True, null=True)
    plus_calibracao = models.CharField(max_length=1, blank=True, null=True)
    plus_outro = models.CharField(max_length=100, blank=True, null=True)
    plus_valor = models.FloatField(blank=True, null=True)
    plus_titulo = models.CharField(max_length=100, blank=True, null=True)
    plus_observacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_plus_service'
        unique_together = (('plus_codigo', 'cli_codigo', 'os_codigo'),)


class OsProvasOutro(models.Model):
    fpo_codigo = models.AutoField(primary_key=True)
    imp_codigo = models.PositiveIntegerField()
    os_codigo = models.PositiveIntegerField(blank=True, null=True)
    fpo_quantidade = models.PositiveIntegerField(blank=True, null=True)
    fpo_altura = models.FloatField(blank=True, null=True)
    fpo_largura = models.FloatField(blank=True, null=True)
    fpo_valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_provas_outro'


class OsProvasPadrao(models.Model):
    fpp_codigo = models.AutoField(primary_key=True)
    imp_codigo = models.PositiveIntegerField()
    fpp_quantidade = models.PositiveIntegerField(blank=True, null=True)
    fpp_formato = models.PositiveIntegerField(blank=True, null=True)
    fpp_valor = models.FloatField(blank=True, null=True)
    os_codigo = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os_provas_padrao'


class OsStatus(models.Model):
    sts_status = models.CharField(primary_key=True, max_length=1)
    sts_nome = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'os_status'


class ServicosUtilizados(models.Model):
    srv_codigo = models.AutoField(primary_key=True)
    srv_nome = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'servicos_utilizados'


class Up(models.Model):
    up_codigo = models.CharField(primary_key=True, max_length=10)
    up_nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'up'


class Usuarios(models.Model):
    usu_login = models.CharField(primary_key=True, max_length=60)
    usu_nome = models.CharField(max_length=60, blank=True, null=True)
    usu_senha = models.CharField(max_length=32)
    usu_status = models.CharField(max_length=1, blank=True, null=True)
    usu_tipo = models.CharField(max_length=50, blank=True, null=True)
    usu_lastlogin = models.DateTimeField(blank=True, null=True)
    up_codigo = models.CharField(max_length=15, blank=True, null=True)
    usu_excluido = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class UsuariosPermissoes(models.Model):
    usu_login = models.CharField(primary_key=True, max_length=60)
    per_cad_usuario = models.CharField(max_length=1, blank=True, null=True)
    per_con_usuario = models.CharField(max_length=1, blank=True, null=True)
    per_cad_cliente = models.CharField(max_length=1, blank=True, null=True)
    per_con_cliente = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_permissoes'
