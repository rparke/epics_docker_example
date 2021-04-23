from malcolm.yamlutil import make_block_creator, check_yaml_names

pmac_manager_block = make_block_creator(__file__, "pmac_manager_block.yaml")
scan_block = make_block_creator(__file__, "scan_block.yaml")
odin_scan_block = make_block_creator(__file__, "odin_scan_block.yaml")

__all__ = check_yaml_names(globals())
