import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";
import { useEffect, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { user } from "@web/core/user";
import { getCurrency } from "@web/core/currency";
import { imageUrl } from "@web/core/utils/urls";

patch(NavBar.prototype, {
  setup() {
    super.setup();
    this.commandService = useService("command");
    this.body = document.querySelector("body");
    this.user = user;
    this.state = useState({
      ...this.state,
      isSidebarOpen: false,
      companyLogo: imageUrl("res.company", this.user.activeCompany.id, "logo", {
        width: 256,
        height: 256,
      }),
      companyCurrency: getCurrency(this.user.activeCompany.currency_id),
      userAvatar: imageUrl("res.users", this.user.userId, "avatar_128", {
        width: 256,
        height: 256,
      }),
      userName: this.user.name,
      userLogin: this.user.login,
    });
    console.log(this);
    useEffect(
      () => {
        this.body.style.paddingLeft = this.state.isSidebarOpen
          ? "15em"
          : this.env.isSmall
            ? "0em"
            : "4em";
      },
      () => [this.state.isSidebarOpen, this.env.isSmall],
    );
  },

  toggleSidebar() {
    this.state.isSidebarOpen = !this.state.isSidebarOpen;
    this.body.style.paddingLeft = this.state.isSidebarOpen
      ? "15em"
      : this.env.isSmall
        ? "0em"
        : "4em";
  },

  handleCompanyClick() {
    this.actionService.doAction({
      res_model: "res.company",
      res_id: this.user.activeCompany.id,
      views: [[false, "form"]],
      type: "ir.actions.act_window",
      view_mode: "form",
      target: "new",
      name: "My Company",
      context: {
        form_view_ref: "base.view_company_form",
      },
    });
  },

  handleSearchClick() {
    this.commandService.openMainPalette({ searchValue: "/" });
  },
});
