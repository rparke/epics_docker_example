from malcolm.yamlutil import make_include_creator, check_yaml_names

BL4xP_template = make_include_creator(
    __file__, "BL4xP_template.yaml")

__all__ = check_yaml_names(globals())
